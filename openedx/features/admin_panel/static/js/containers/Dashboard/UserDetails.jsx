import React from 'react'

import {
    Card,
    CardBody,
    CardTitle,
    CardText,
    Col,
    Row
} from 'reactstrap';

export default function UserDetails(props) {
    return (
        <Card style={{
            padding: '30px'
        }}>
            <CardTitle>Lead Admin</CardTitle>
            <CardBody>
                <Row>
                    <Col md='4'><img style={{
                        width: 'inherit'
                    }} src='https://sms.northhills.edu.pk/uploads/website/officers/anonymous-user.png' /></Col>
                    <Col md='auto'>
                        <Row>
                            <span className='lead'>Name:</span>
                        </Row>
                        <Row>
                            <span>John Doe</span>
                        </Row>
                        <Row>
                            <span className='lead'>e-mail:</span>
                        </Row>
                        <Row>
                            <span>edx@example.com</span>
                        </Row>
                        <Row>
                            <span className='lead'>Phone:</span>
                        </Row>
                        <Row>
                            <span>12345678</span>
                        </Row>
                    </Col>
                </Row>
            </CardBody>
        </Card>
    )
}
