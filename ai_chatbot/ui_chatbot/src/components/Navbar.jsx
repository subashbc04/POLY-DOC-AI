import React from 'react'
import bgvideo from '../assets/video.mp4'

const Navbar = () => {
  return (

    <div>

      <video autoPlay muted loop playsInline
       className="fixed inset-0 w-full h-full object-cover -z-10">
        <source src={bgvideo} type="video/mp4" />
      </video>


      <div className='flex justify-between px-5'>

        <h2 className='text-blue-500 font-bold text-3xl p-3 relative '>PolyDocAI</h2>
        <ul className='flex gap-6 p-3 text-blue-500 text-lg'>
            <li><a href='#'>Sign in</a></li>
            <li><a href='#' className='bg-blue-500 p-2 rounded-md text-white text-lg'>Get Started</a></li>
        </ul>

      </div>  
    </div>
    
    
  )
}

export default Navbar