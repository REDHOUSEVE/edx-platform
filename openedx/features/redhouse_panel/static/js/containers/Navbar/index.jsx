import React from 'react';
import { Link, useLocation } from 'react-router-dom';

import {
    Button,
    Form,
    Input,
    InputGroup,
    InputGroupAddon,
    InputGroupText,
    Navbar,
    Nav,
    NavItem,
    NavLink,

} from 'reactstrap';


export default function PanelNavbar(props) {
    const location = useLocation();
    const isPeoplePage = location.pathname === '/people';

    const PeoplePageItems = isPeoplePage ? (
        <Form inline className='w-100'>
            <div className='d-flex justify-content-end w-50'>
                <InputGroup>
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText>
                            <i className="fa fa-search" aria-hidden="true"></i>
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input placeholder="Search Profile" />
                </InputGroup>
            </div>

            <div className='d-flex justify-content-end w-50'>
                <span className='m-1 btn btn-outline-secondary'>Add Users</span>
                <span className='m-1 btn btn-outline-secondary'>Export all  to CSV</span>
            </div>
        </Form>
    ) : '';

    return (
        <div>
            <Navbar color='light' light expand='md'>
                <Nav className='m-auto w-100' navbar>
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
                    {PeoplePageItems}
                </Nav>
            </Navbar>
        </div>
    )
}
