import React from 'react';
import { Card } from 'reactstrap';
import StatsBox from './StatsBox';

export default function StatsBar(props) {
    return (
        <Card>
            <ul className='stats-list'>
                <li>
                    <StatsBox number={'165'} text={'Teachers/Admins'} />
                </li>
                <li>
                    <StatsBox number={'2,129'} text={'Student Accounts'} />
                </li>
                <li>
                    <StatsBox number={'1,000'} text={'Public Accounts'} />
                </li>
            </ul>
        </Card>
    )
}
