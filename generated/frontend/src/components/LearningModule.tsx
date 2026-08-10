import type { ReactNode } from "react";




interface LearningModuleProps {

  children?: ReactNode;
}

export default function LearningModule({

  children,
}: LearningModuleProps) {
  return (
    <section


    >
      <div>
        LearningModule
      </div>

      {children}
    </section>
  );
}
