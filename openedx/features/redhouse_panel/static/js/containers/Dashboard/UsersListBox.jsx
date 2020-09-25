import React from 'react'

import {
    Card,
    CardTitle,
    CardBody,
    CardText,
    Row,
    Col
} from 'reactstrap';


export default function UsersListBox({ title, data }) {
    return (
        <div>
            <Card>
                <CardTitle>{title}</CardTitle>
                <CardBody>
                    <CardText>
                        <ul className='overflow-auto box-list'>
                            {data.map((row, idx) => (
                                <li key={idx}>
                                    <Row>
                                        <Col md={2}>
                                            <img className='w-100 h-100 rounded-circle' src='https://rnmu.rw/wp-content/uploads/2019/10/man-300x300.png'/>
                                        </Col>
                                        <Col md={6}>
                                            <span>{row.name}</span>
                                        </Col>
                                        <Col md={4}>
                                            <span className='btn btn-primary'>View</span>
                                        </Col>
                                    </Row>
                                </li>
                            ))}
                        </ul>
                        <Row>
                            <Col className='d-flex justify-content-center'>
                                <span class='btn btn-outlined-secondary center'>View All</span>
                            </Col>
                        </Row>
                    </CardText>
                </CardBody>
            </Card>
        </div>
    )
}
