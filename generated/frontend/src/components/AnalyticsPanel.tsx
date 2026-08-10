import type { ReactNode } from "react";




interface AnalyticsPanelProps {

  children?: ReactNode;
}

export default function AnalyticsPanel({

  children,
}: AnalyticsPanelProps) {
  return (
    <section


    >
      <div>
        AnalyticsPanel
      </div>

      {children}
    </section>
  );
}
