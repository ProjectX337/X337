import type { ReactNode } from "react";




interface DataTableProps {

  children?: ReactNode;
}

export default function DataTable({

  children,
}: DataTableProps) {
  return (
    <section


    >
      <div>
        DataTable
      </div>

      {children}
    </section>
  );
}
