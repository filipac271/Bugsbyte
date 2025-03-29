import React from 'react'
import Logo from "./assets/laftale.jpeg"

type Props = {}

const Navbar = (props: Props) => {
  const flexBetween = "flex items-center justify-between";
  return (
    <nav>
      <div className={`${flexBetween} sticky top-0 z-30 w-full py-5 bg-green-200`}>
        <div className={`${flexBetween} w-full gap-16`}>
        
          {/**Lado esquerdo-> Home */}
          <div className={'${flexBetween}'}>
            {/**Vai ter a imagem aqui */}
            {/* <img alt="logo"
            src={Logo}
            className=''/> */}
            Laf leaf
          </div>
          {/**Lada direito o tal do botao */}
          <div className={`${flexBetween} `}>
            {/** o tal botao*/}
            <div className={`${flexBetween}`}>
            <button className='rounded-full bg-primary-100 px-10 py-2 hover:bg-green-500'>
              empresa
            </button>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar