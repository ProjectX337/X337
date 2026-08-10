import type { ReactNode } from "react";




interface NavbarProps {

  children?: ReactNode;
}

export default function Navbar({

  children,
}: NavbarProps) {
  return (
    <section


    >
      <div>
        Navbar
      </div>

      {children}
    </section>
  );
}
