import React, { useEffect } from 'react';
import { Button } from 'react-bootstrap';
import { useSearchParams } from 'react-router-dom';
import axios from 'axios';
import { Container } from 'react-bootstrap';


import { Event } from './Event';
import { API_URL } from './constants';

import './Events.css';

function findEvents() {
    axios.get('api/events', { 
            params: {
                city: 'San Jose, CA'
            }
        })
        .then((response) => {
            console.log(response);
        })
        .catch(() => {
            console.log("There was an error.");
        });
}

function Events() {
    const [searchParams, _] = useSearchParams();

    useEffect(() => {
        console.log('In useEffect');
        axios.get('api/login', {
                params: {
                    code: searchParams.get('code')
                }
            })
            .then((response) => {
                console.log('The api was called successfully.')
                //console.log(response);
            })
            .catch(() => {
                console.log('There was an error when calling the api.')
            });
    }, []);

/*     useEffect(() => {
        console.log("In 2nd useEffect");
        axios.get('api/events')
            .then((response) => {
                console.log(response);
            })
            .catch(() => {
                console.log('There was an error when calling the api.');
            })
    }, []); */

    return (
        <Container>
            <h2>This is the Events page.</h2>
            <div class="input-group rounded">
                <input type="search" class="form-control rounded" placeholder="Search by city"/>
            </div>

            <Button onClick={findEvents}>
                City
            </Button>
        </Container>

    );
}

export default Events;