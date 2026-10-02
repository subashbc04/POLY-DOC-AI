import { useState } from 'react';
import axios from "axios";


function cleanText(text) {
  return String(text)
    .replace(/\\n/g, "\n")            
    .replace(/^#{1,6}\s*/gm, "")      
    .replace(/\*\*/g, "")             
    .replace(/^\s*[-*]\s+/gm, "- ");  
}

function Analyse() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [chatbot, setChatbot] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append("document", file);
    data.append("queries", question);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/analyse/", data);


      const raw = typeof response.data === "string"
        ? response.data
        : response.data.ai_analysis;

      setChatbot(cleanText(raw));
    } catch (error) {
      console.log(error);
    }
  };

  return (
     <div className="flex mt-25 flex-col items-center justify-center gap-5   px-4 py-10">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md space-y-5 rounded-2xl bg-black/75 p-8 shadow-xl"
      >
        <h2 className="text-center text-2xl font-bold text-blue-600">
          Analyse Document
        </h2>

        <div>
          <label className="mb-1 block text-sm font-medium text-white">
            Upload Document
          </label>
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            className="w-full rounded-lg border border-gray-300 p-2 text-sm  text-white
                       file:mr-3 file:rounded-md file:border-0 file:bg-blue-600
                       file:px-3 file:py-1.5 file:text-white hover:file:bg-blue-700 hover:cursor-pointer"
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-white">
            Questions
          </label>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask something about the document"
            className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-white
                       focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-300 hover:cursor-pointer"
          />
        </div>

        <button
          type="submit"
          className="w-full rounded-lg bg-blue-600 py-2.5 font-medium text-white
                     transition hover:bg-blue-700 hover:cursor-pointer"
        >
          Analyse
        </button>
      </form>

      {chatbot && (
        <pre className="w-full max-w max-h-96 overflow-auto rounded-2xl bg-black/75 p-6 text-sm text-white shadow-xl whitespace-pre-wrap">
          {chatbot}
        </pre>
      )}
    </div>
  );
}

export default Analyse;