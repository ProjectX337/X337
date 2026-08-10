import type { ReactNode } from "react";




interface AITutorChatProps {

  children?: ReactNode;
}

export default function AITutorChat({

  children,
}: AITutorChatProps) {
  return (
    <section


    >
      <div>
        AITutorChat
      </div>

      {children}
    </section>
  );
}
