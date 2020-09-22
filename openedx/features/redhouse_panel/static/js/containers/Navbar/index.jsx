import React from 'react';
import ReactDOM from 'react-dom';
import { Link } from 'react-router-dom';

import {
    Collapse,
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,

} from 'reactstrap';


export default function PanelNavbar(props) {
    return (
        <div>
            <Navbar color='light' light expand='md'>
                <Nav className='mr-auto' navbar>
                    <NavItem>
                        <NavLink tag={Link} to='/'>
                            Admin
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink tag={Link} to='/people'>
                            People
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink tag={Link} to='/settings'>
                            Settings
                        </NavLink>
                    </NavItem>
                </Nav>
            </Navbar>
        </div>
    )
}
