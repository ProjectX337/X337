import type { ReactNode } from "react";




interface SidebarProps {

  children?: ReactNode;
}

export default function Sidebar({

  children,
}: SidebarProps) {
  return (
    <section


    >
      <div>
        Sidebar
      </div>

      {children}
    </section>
  );
}
