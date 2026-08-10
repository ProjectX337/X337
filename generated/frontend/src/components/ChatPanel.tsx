import type { ReactNode } from "react";




interface ChatPanelProps {

  children?: ReactNode;
}

export default function ChatPanel({

  children,
}: ChatPanelProps) {
  return (
    <section


    >
      <div>
        ChatPanel
      </div>

      {children}
    </section>
  );
}
