import React from 'react'

import {
    Card,
    CardBody,
    CardTitle,
    CardText,
    Col,
    Row
} from 'reactstrap';

export default function SchoolInfo(props) {
    return (
        <Card>
            <CardTitle>School Information</CardTitle>
            <CardBody>
                <Row>
                    <Col sm='12' md='4'>
                        <img
                            className='rounded-circle w-100'
                            src='https://sms.northhills.edu.pk/uploads/website/officers/anonymous-user.png'
                        />
                    </Col>
                    <Col sm='12' md='auto'>
                        <Row>
                            <span>Name:</span>
                        </Row>
                        <Row>
                            <span>John Doe</span>
                        </Row>
                        <Row>
                            <span>Address:</span>
                        </Row>
                        <Row>
                            <span>15 Yemen Road, Yemen</span>
                        </Row>
                    </Col>
                </Row>
            </CardBody>
        </Card>
    )
}
