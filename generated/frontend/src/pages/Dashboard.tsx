import AppShell from "../AppShell";


import Navbar from "../components/Navbar";

import Sidebar from "../components/Sidebar";

import MetricCard from "../components/MetricCard";

import DashboardCard from "../components/DashboardCard";

import DataTable from "../components/DataTable";

import ChatPanel from "../components/ChatPanel";

import CommandPalette from "../components/CommandPalette";


export default function Dashboard() {
  return (
    <AppShell>
      <main className="min-h-screen">
        <h1>Dashboard</h1>

        <section className="space-y-4">

          <Navbar />

          <Sidebar />

          <MetricCard />

          <DashboardCard />

          <DataTable />

          <ChatPanel />

          <CommandPalette />

        </section>
      </main>
    </AppShell>
  );
}
