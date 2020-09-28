import React from 'react';

import {
    Container,
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
        <Container fluid>
            <div className='panel-dashboard'>
                <StatsBar />
                <div>
                    <Row className='ml-0'>
                        <Col className='info-box'>
                            <SchoolInfo />
                        </Col>

                        <Col className='info-box'>
                            <UserDetails />
                        </Col>
                    </Row>
                    <Row className='ml-0'>
                        <Col className='p-0'>
                            <PermissionsManager />
                        </Col>
                    </Row>
                    <Row className='ml-0'>
                        <Col className='info-box'>
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
                        <Col className='info-box'>
                            <UsersListBox title='Teachers' data={[
                                { name: 'John Doe1' },
                                { name: 'John Doe' },
                                { name: 'John Doe' },
                                { name: 'John Doe' },
                            ]} />
                        </Col>


                    </Row>
                    <Row className='ml-0'>
                        <Col className='info-box'>
                            <AdvancedSettings />
                        </Col>
                    </Row>
                </div>
            </div>
        </Container>
    )
}
