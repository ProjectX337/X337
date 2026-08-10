import type { ReactNode } from "react";




interface CommandPaletteProps {

  children?: ReactNode;
}

export default function CommandPalette({

  children,
}: CommandPaletteProps) {
  return (
    <section


    >
      <div>
        CommandPalette
      </div>

      {children}
    </section>
  );
}
