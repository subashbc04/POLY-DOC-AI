import { useState } from 'react'
import Navbar from './components/navbar'
import Analyse from './components/Analyse'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar/>
      <Analyse/>
    </>
  )
}

export default App
