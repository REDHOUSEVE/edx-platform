import React from 'react'

import {
    Card,
    CardTitle,
    CardBody,
    Col,
    Table,
    CardFooter
} from 'reactstrap';

export default function UsersListBox({ title, data }) {
    return (
        <Card>
            <CardTitle><h2>{title}</h2></CardTitle>
            <CardBody>
                <Table className='table-striped'>
                    <tbody>
                    {data.map((row, idx) => (
                        <tr key={idx}>
                            <td className='img-col'>
                                <img src='https://rnmu.rw/wp-content/uploads/2019/10/man-300x300.png' height='39' width='39' />
                            </td>
                            <td>
                                <strong>{row.name}</strong>
                            </td>
                            <td className='btn-col'>
                                <span className='btn btn-outline-default'>View</span>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </Table>
            </CardBody>
            <CardFooter>
                <span className='text-link'>View All</span>
            </CardFooter>
        </Card>
    )
}
