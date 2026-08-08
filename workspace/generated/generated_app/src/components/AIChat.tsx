

import React, {
    useState
} from "react";

import aiTutorService
from "../services/aiTutorService";




interface AIChatProps {


    userId: string;

    lessonId: string;


}



export default function AIChat(

props: AIChatProps

) {





const [
    messages,
    setMessages
] = useState([]);




const [
    input,
    setInput
] = useState([]);








function sendMessage(){

    console.log(
        "sendMessage"
    );

}





return (


<div className="AIChat">

    <h2>
        AIChat
    </h2>

    <p>
        AI conversational tutoring interface
    </p>

</div>


)

}

