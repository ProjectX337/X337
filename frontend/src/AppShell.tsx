import { RouterProvider } from "react-router-dom";
import { router } from "./router";

export default function AppShell() {
  return (
    <RouterProvider router={router} />
  );
}