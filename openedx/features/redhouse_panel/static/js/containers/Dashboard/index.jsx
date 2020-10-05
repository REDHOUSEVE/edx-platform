import React from 'react';

import {
    Row,
    Col,
} from 'reactstrap';

import StatsBar from './StatsBar';
import UserDetails from './UserDetails';
import SchoolInfo from './SchoolInfo';
import PermissionsManager from './PermissionsManager';
import UsersListBox from './UsersListBox';
import AdvancedSettings from './AdvancedSettings';

export default function Dashboard(props) {
    return (
        <div className='panel-dashboard'>
            <StatsBar />
            <div>
                <Row className='align-items-stretch'>
                    <Col md='6' className='info-box'>
                        <SchoolInfo />
                    </Col>
                    <Col md='6' className='info-box'>
                        <UserDetails />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <PermissionsManager />
                    </Col>
                </Row>
                <Row>
                    <Col md='6' className='users-box'>
                        <UsersListBox title='Students' data={[
                            { name: 'John Doe1' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                        ]} />
                    </Col>
                    <Col md='6' className='users-box'>
                        <UsersListBox title='Teachers' data={[
                            { name: 'John Doe1' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                            { name: 'John Doe' },
                        ]} />
                    </Col>
                </Row>
                <Row>
                    <Col className='settings-box'>
                        <AdvancedSettings />
                    </Col>
                </Row>
            </div>
        </div>
    )
}
