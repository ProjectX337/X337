import type { ReactNode } from "react";




interface MetricCardProps {

  children?: ReactNode;
}

export default function MetricCard({

  children,
}: MetricCardProps) {
  return (
    <section


    >
      <div>
        MetricCard
      </div>

      {children}
    </section>
  );
}
