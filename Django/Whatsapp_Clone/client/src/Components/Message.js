import React from "react";

export default function Message({ text, sent }) {
    return (
        <div className={`message ${sent? 'sent': 'received'}`}>
            <div className="message-buble">
                {text}
            </div>
        </div>
    )
}