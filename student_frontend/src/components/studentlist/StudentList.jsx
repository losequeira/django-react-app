import React, { useEffect, useState } from 'react';
import './StudentList.css'

const Student = () => {
    const [ students, setStudents ] = useState([])
    const studentsAPIBaseURL = 'http://localhost:8000/api'

    useEffect(() => {
        fetchStudents();
    }, []);

    const fetchStudents = () => {
        fetch(`${studentsAPIBaseURL}/students/`)
        .then(response => response.json())
        .then(json => setStudents(json))
    }

    return (
        <div className="container">
            <table>
                <caption> Student List</caption>
                <thead>
                    <tr>
                        <th scope="column">Name</th>
                        <th scope="column">Last Name</th>
                        <th scope="column">Address (State, City, ZIPCODE)</th>
                    </tr>
                </thead>
                <tbody>
                {
                    students.map(student =>
                        <tr key={student.id}>
                            <td>{student.name}</td>
                            <td>{student.lastname}</td>
                            <td>{
                                `${student.address.state},
                                ${student.address.city},
                                ${student.address.zipcode}`
                            }
                            </td>
                        </tr>
                    )
                }
                </tbody>
            </table>
        </div>
    );
};

export default Student;