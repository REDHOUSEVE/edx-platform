import React, { useState } from 'react';

import {
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
                <CardTitle>PROFILES AND PRIVILEGES</CardTitle>
                <Table>
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
                                <th scope='row'>{permission}</th>
                                {ROLES.map((role, idxR) => (
                                    <td key={role}>
                                        <input
                                            type='checkbox'
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
            </Card>
        </div>
    )
}
