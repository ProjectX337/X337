import Editor from "@monaco-editor/react";


interface CodeEditorProps {

    code: string;

    fileName: string;

}


export default function CodeEditor(
    {
        code,
        fileName
    }: CodeEditorProps
){

    const language =
        fileName.endsWith(".tsx")
        ? "typescript"
        :
        fileName.endsWith(".ts")
        ? "typescript"
        :
        "javascript";


    return (

        <div
            style={{
                height:"70vh",
                border:"1px solid #333"
            }}
        >

            <Editor

                height="100%"

                language={language}

                theme="vs-dark"

                value={code}

                options={{
                    fontSize:14,
                    minimap:{
                        enabled:false
                    },
                    automaticLayout:true
                }}

            />

        </div>

    );

}
