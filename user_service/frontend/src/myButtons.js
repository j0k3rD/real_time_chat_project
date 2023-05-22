import React from "react"
import "./myButtons.css"

export function MyButtons() {
    return (
        <div>
        <a href="http://user.chat.localhost/login">
          <button className="my-button">
            Login
          </button>
        </a>
        <a href="http://user.chat.localhost/register">
          <button className="my-button">
            Register
          </button>
        </a>
        </div>
    )
}