import React from 'react';
import { BackTop } from 'antd';
import { Link } from 'react-router-dom';

export class Appfooter  {
  render() {
    return (
      <div className='fluid-container'>
        <div className='footer'>
            <div className='logo'>
                <i className='fas fa-home fa-2x'></i>
                <Link to="/">Real Estate</Link>         
            </div>
            <ul className='social-link'>
                <li>
                    <a href="https://www.twitter.com/" >
                        <i className='fab fa-twitter'></i>
                    </a>
                </li>
            </ul>
        </div> 
      </div>
    )
  }
}

export default Appfooter
