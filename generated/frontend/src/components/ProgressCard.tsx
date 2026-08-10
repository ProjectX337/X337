import type { ReactNode } from "react";




interface ProgressCardProps {

  children?: ReactNode;
}

export default function ProgressCard({

  children,
}: ProgressCardProps) {
  return (
    <section


    >
      <div>
        ProgressCard
      </div>

      {children}
    </section>
  );
}
