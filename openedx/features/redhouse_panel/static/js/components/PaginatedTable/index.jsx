import React, { useState } from 'react';

import {
    Table
} from 'reactstrap';


export default function PaginatedTable({ header, data, renderRow = null, renderHeader = null }) {
    const [state, setState] = useState({
        currentPage: 1,
    });

    const defaultRenderHeader = header => {
        return (
            <thead>
                <tr>
                    {header.map((value, idx) => (
                        <th key={idx}>{value}</th>
                    ))}
                </tr>
            </thead>
        )
    }


    const defaultRenderRow = (row, idx) => {
        return (
            <tr key={idx}>
                {Object.values(row).map((value, idx) => (
                    <td key={idx}>{value}</td>
                ))}
            </tr>
        )
    }

    return (
        <div>
            <Table striped>
                {header ? (
                    renderHeader ?
                        renderHeader(header) :
                        defaultRenderHeader(header)
                ) : ''}
                <tbody>
                    {renderRow ? data.map(renderRow) : data.map(defaultRenderRow)}
                </tbody>
            </Table>
        </div>
    )
}
