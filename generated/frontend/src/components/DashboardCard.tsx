import type { ReactNode } from "react";




interface DashboardCardProps {

  children?: ReactNode;
}

export default function DashboardCard({

  children,
}: DashboardCardProps) {
  return (
    <section


    >
      <div>
        DashboardCard
      </div>

      {children}
    </section>
  );
}
