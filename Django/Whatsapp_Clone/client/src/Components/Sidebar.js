import React, { useEffect, useState } from "react";
import axios from 'axios'
import { Box, LinearProgress, List } from "@mui/material";
import UserItem from "./UserItem";

function Sidebar() {
    const BASE_URL = "http://127.0.0.1:8000"
    const [userList, setuserList] = useState([]);
    const [userLoader, setUserLoader] = useState(true)
    const getAuthToken = () => {
        const cookies = document.cookie.split('; ')
        const token = {'name': null};
        cookies.forEach((cookie) => {
            const [name, value] = cookie.trim().split('=');
            if (name === 'token') {
                token.name = value;
            }
        })
        return token.name;
    }
    useEffect(() => {
        const authToken = getAuthToken()
        console.log(authToken)
        if (authToken) {
            axios.get(`${BASE_URL}/api/users/`, {
                headers: {
                    Authorization: `Bearer ${authToken}`
                }
            }).then((res) => { 
                setuserList(res.data)
                setUserLoader(false)
            }).catch((err) => {
                console.log("Error getting user list", err)
            })
        }
    }, [])
    return (
        <div className="sidebar">
            {userLoader ? <Box sx={{width: '100%'}}>
                    <LinearProgress/>
                </Box>:
                <List sx={{width: '100%', maxWidth: '360', bgcolor: 'background.paper'}}>
                    {userList.map((user, index) => (
                        <UserItem key={index} email={user.email} name={`${user.first_name} ${user.last_name}`} id={user.id}/>
                    ))}
                </List>
            }
        </div>
    )
}

export default Sidebar;
