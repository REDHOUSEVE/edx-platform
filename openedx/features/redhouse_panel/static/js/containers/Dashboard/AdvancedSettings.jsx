import React from 'react'

import {
    Button,
    Card,
    CardTitle,
    CardText,
    Row,
    Col
} from 'reactstrap';


export default function AdvancedSettings(props) {
    return (
        <Card>
            <Row className='align-items-center'>
                <Col md="8">
                    <CardTitle><h2>ADVANCED SETTINGS</h2></CardTitle>
                    <CardText>
                        *Note: Only Lead Admin can see/change advanced settings.
                    </CardText>
                </Col>
                <Col md="4" className='text-center'>
                    <Button color='outline-primary' size='lg'>VIEW SETTINGS</Button>
                </Col>
            </Row>
        </Card>
    )
}
