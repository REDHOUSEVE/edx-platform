import React from 'react';

import {
    Container,
    Row,
    Col,
    Button
} from 'reactstrap';

import PaginatedTable from '../../components/PaginatedTable';

const MOCK_USERS_DATA = [
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
    {
        fullName: 'D',
        profile: 'Admin',
        email: 'abc@example.com',
        level: 'N/A',
    },
]
export default function PeoplePage(props) {
    const renderHeader = header => {
        return (
            <thead>
                <th>
                    <input type="checkbox" checked={false} />
                    <span>All</span>
                </th>
                {header.map((label, idx) => (
                    <th key={idx}>{label}</th>
                ))}
               <th>
                    <span>Sort By</span>
                </th>
            </thead>
        )
    }
    const renderRow = (row, idx) => {
        return (
            <tr key={idx}>
                <td>
                    <input type="checkbox" checked={false} />
                </td>
                {Object.values(row).map((value, idx) => (
                    <td key={idx}>{value}</td>
                ))}
                 <td>
                    <span className='m-1 btn btn-outline-secondary'>Edit</span>
                    <span className='m-1 btn btn-outline-danger'>Delete</span>
                </td>
            </tr>
        )
    }
    return (
        <Container fluid>
            <div className='m-0'>
                <PaginatedTable
                    header={['Full Name', 'Profile', 'Email', 'Level']}
                    renderHeader={renderHeader}
                    renderRow={renderRow}
                    data={MOCK_USERS_DATA}
                />
            </div>
        </Container>
    )
}
