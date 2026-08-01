from core.generators.file_builder import FileBuilder

files = FileBuilder()

files.json(

    "frontend/package.json",

    '{"name":"frontend"}',

)

files.typescript(

    "frontend/src/App.tsx",

    "export default function App() {}",

)

files.markdown(

    "README.md",

    "# Hello",

)

result = files.result()

print()

for file in result.files:

    print(

        file.path,

        "|",

        file.language,

    )
