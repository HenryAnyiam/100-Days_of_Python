import React from "react";
import Message from "./Message";
import MessageInput from "./MessageInput";

export default function ChatArea() {
    return (
        <div className="chat-area">
            <div className="chat-header"></div>
            <div className="messages">
                <Message text="Hey, How are you?" sent/>
                <Message text="I am alright"/>
            </div>
            <MessageInput/>
        </div>
    )
}