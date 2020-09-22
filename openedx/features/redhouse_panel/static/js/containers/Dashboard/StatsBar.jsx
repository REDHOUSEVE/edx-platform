import React from 'react';

import {
    Card,
    Row,
    Col,
} from 'reactstrap';

import StatsBox from './StatsBox';


export default function StatsBar(props) {
    return (
        <Card>
            <Row>
                <Col sm={{ size: 'auto', offset: 3 }}>
                    <StatsBox number={1} text={'Teachers/Admins'} />
                </Col>
                <Col sm={{ size: 'auto', offset: 1 }}>
                    <StatsBox number={1} text={'Student Accounts'} />
                </Col>
                <Col sm={{ size: 'auto', offset: 1 }}>
                    <StatsBox number={1} text={'Public Accounts'} />
                </Col>
            </Row>
        </Card>
    )
}
