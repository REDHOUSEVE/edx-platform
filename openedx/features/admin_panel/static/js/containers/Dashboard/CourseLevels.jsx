import React from 'react'

import {
    Card,
    CardTitle,
    CardBody,
    CardText
} from 'reactstrap';


export default function CourseLevels(props) {
    const renderLevels = () => {
        const levels = [];
        for (let i = 1; i < 6; i++) {
            levels.push(
                <li key={i}>
                    {`${i}th Grade`}
                </li>
            )
        }
        return levels;
    }
    return (
        <div>
            <Card>
                <CardTitle>LEVEL</CardTitle>
                <CardBody>
                    <CardText>
                        {
                            'This level information is attached to courses when these are created.' +
                            ' Levels are ideal to map courses into your institution level system.'
                        }
                    </CardText>
                    <ol>
                        {renderLevels()}
                    </ol>
                </CardBody>
            </Card>
        </div>
    )
}
