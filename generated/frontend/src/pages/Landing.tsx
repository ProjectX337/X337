import AppShell from "../AppShell";


import Navbar from "../components/Navbar";

import Sidebar from "../components/Sidebar";

import MetricCard from "../components/MetricCard";

import DashboardCard from "../components/DashboardCard";

import DataTable from "../components/DataTable";

import ChatPanel from "../components/ChatPanel";

import CommandPalette from "../components/CommandPalette";

import AITutorChat from "../components/AITutorChat";

import ProgressCard from "../components/ProgressCard";

import LearningModule from "../components/LearningModule";

import AnalyticsPanel from "../components/AnalyticsPanel";


export default function Landing() {
  return (
    <AppShell>
      <main className="min-h-screen">
        <h1>Landing</h1>

        <section className="space-y-4">

          <Navbar />

          <Sidebar />

          <MetricCard />

          <DashboardCard />

          <DataTable />

          <ChatPanel />

          <CommandPalette />

          <AITutorChat />

          <ProgressCard />

          <LearningModule />

          <AnalyticsPanel />

        </section>
      </main>
    </AppShell>
  );
}
