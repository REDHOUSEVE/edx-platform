import React from 'react';
import ReactDOM from 'react-dom';
import { NavLink } from 'react-router-dom';

export default function PanelNavbar(props) {
    return (
        <nav className='dashboard-nav'>
            <ul>
                <li>
                    <NavLink to='/' activeClassName='active'>
                        <span className='icon-box'>
                            <img src='../../../static/images/icon-admin.svg' />
                        </span>
                        Admin
                    </NavLink>
                </li>
                <li>
                    <NavLink to='/people' activeClassName='active'>
                        <span className='icon-box'>
                            <img src='../../../static/images/icon-team.svg' />
                        </span>
                        People
                    </NavLink>
                </li>
                <li>
                    <NavLink to='/settings' activeClassName='active'>
                        <span className='icon-box'>
                            <img src='../../../static/images/icon-settings.svg' />
                        </span>
                        Settings
                    </NavLink>
                </li>
            </ul>
        </nav>
    )
}
