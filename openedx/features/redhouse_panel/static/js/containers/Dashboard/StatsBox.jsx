import React from 'react';

import {
    Row,
} from 'reactstrap';


export default function StatsBox({ number, text }) {
    return (
        <div>
            <Row
                className={[
                    'justify-content-center',
                    'font-weight-bolder'
                ]}
            >
                <span className='display-4'>
                    {number}
                </span>
            </Row>
            <Row className='text-center'>
                <p className='text-muted'>{text}</p>
            </Row>
        </div>
    )
}
