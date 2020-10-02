import React from 'react';

export default function StatsBox({ number, text }) {
    return (
        <div>
            <strong className='number'>{number}</strong>
            <span className='text'>{text}</span>
        </div>
    )
}
