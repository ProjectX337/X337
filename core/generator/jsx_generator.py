class JSXGenerator:


    def generate(
        self,
        component
    ):


        if component.name == "AIChat":

            return """

<div className="AIChat">


<div className="messages">

{messages.map(
(message,index)=>(
<p key={index}>
{message}
</p>
)

)}

</div>



<input

value={input}

onChange={
e=>setInput(
e.target.value
)
}

/>



<button

onClick={
sendMessage
}

>

Send

</button>



</div>

"""


        return f"""

<div className="{component.name}">

<h2>

{component.name}

</h2>


</div>

"""