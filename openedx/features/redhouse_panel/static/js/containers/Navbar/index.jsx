import React from 'react';
import ReactDOM from 'react-dom';
import { NavLink } from 'react-router-dom';

import AdminIcon from '../../../images/icon-admin.svg';
var logoTwo = require('svg-inline-loader?classPrefix!../../../images/icon-admin.svg');

import {
    Collapse,
    Navbar,
    NavbarBrand,
    Nav,
    NavItem
} from 'reactstrap';

export default function PanelNavbar(props) {
    console.log(logoTwo, "AdminIcon");
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
