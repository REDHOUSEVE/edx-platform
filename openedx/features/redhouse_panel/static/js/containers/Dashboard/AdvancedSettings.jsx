import React from 'react'

import {
    Button,
    Card,
    CardTitle,
    CardBody,
    CardText
} from 'reactstrap';


export default function AdvancedSettings(props) {
    return (
        <div>
            <Card>
                <CardTitle>ADVANCED SETTINGS</CardTitle>
                <CardBody>
                    <CardText>
                        *Note: Only Lead Admin can see/change advanced settings.
                    </CardText>
                    <div className='w-100 text-center'>
                        <Button color='primary'>VIEW SETTINGS</Button>
                    </div>
                </CardBody>
            </Card>
        </div>
    )
}
