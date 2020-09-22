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
import CourseLevels from './CourseLevels';
import AdvancedSettings from './AdvancedSettings';


export default function Dashboard(props) {
    return (
        <Container fluid>
            <div className='admin-dashboard'>
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
                            <CourseLevels />
                        </Col>

                        <Col className='info-box'>
                            <AdvancedSettings />
                        </Col>
                    </Row>
                </div>
            </div>
        </Container>
    )
}
