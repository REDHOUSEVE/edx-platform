import React, { useState } from 'react';

import {
    CustomInput,
    Card,
    CardTitle,
    Container,
    Row,
    Table,
    Col
} from 'reactstrap';


const PERMISSIONS = [
    'Creator App Permissions',
    'Admin/Profile Management',
    'People Management',
    'Content Management',
    'Banner Management',
    'AssetManagement'
]

const ROLES = [
    'STUDENT',
    'LEAD ADMIN',
    'ADMIN',
    'TEACHER',
    'GUEST ROLE'
]

export default function PermissionsManager(props) {
    const [permissions, setPermissions] = useState({});
    const [state, setState] = useState('test');

    const isChecked = (permission, role) => {
        return permissions[`${permission}-${role}`] || false;
    }
    const toggleChecked = event => {
        const updatedPermissions = {...permissions};
        updatedPermissions[event.target.id] = !!!permissions[event.target.id];
        setPermissions(updatedPermissions);
    }

    return (
        <div>
            <Card>
                <CardTitle><h2>PROFILES AND PRIVILEGES</h2></CardTitle>
                <div className='permissions-table'>
                    <Table className='table-striped'>
                        <thead>
                            <tr>
                                <th></th>
                                {ROLES.map(role => (
                                    <th key={role}>{role}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {PERMISSIONS.map((permission, idxP) => (
                                <tr key={permission}>
                                    <td scope='row'><strong>{permission}</strong></td>
                                    {ROLES.map((role, idxR) => (
                                        <td key={role} className='checkbox-col'>
                                            <CustomInput
                                                type='checkbox'
                                                className='checkbox-lg no-label'
                                                id={`${permission}-${role}`}
                                                checked={isChecked(permission, role)}
                                                onChange={toggleChecked}
                                            />
                                        </td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </Table>
                </div>
            </Card>
        </div>
    )
}
