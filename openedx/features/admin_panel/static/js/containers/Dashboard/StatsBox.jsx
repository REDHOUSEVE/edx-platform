import React from 'react';

import {
    Row,
} from 'reactstrap';


export default function StatsBox({ number, text }) {
    return (
        <div>
            <Row style={{
                justifyContent: 'center',
                fontWeight: 'bolder',
                fontSize: 'xx-large'
            }}>{number}</Row>
            <Row style={{
                textAlign: 'center'
            }}>
                <p className='text-muted'>{text}</p>
                </Row>
        </div>
    )
}
