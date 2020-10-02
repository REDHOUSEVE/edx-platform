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
            <CardTitle><h2>School Information</h2></CardTitle>
            <CardBody>
                <img
                    src='https://sms.northhills.edu.pk/uploads/website/officers/anonymous-user.png'
                />
                <Col>
                    <ul>
                        <li>
                            <span className='title'>Name</span>
                            <span className='text'>Dallas Independent School District</span>
                        </li>
                        <li>
                            <span className='title'>Address</span>
                            <span className='text'>5555 Maple Ave, Dallas, TX 75235</span>
                        </li>
                    </ul>
                </Col>
            </CardBody>
        </Card>
    )
}
