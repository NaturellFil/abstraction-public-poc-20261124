import { authenticate_f6213b8e3a5c } from "./auth.js";
import { operation_f6213b8e3a5c } from "./operation.js";
export function handleRequest_f6213b8e3a5c(request) {
  if (!authenticate_f6213b8e3a5c(request)) return "denied";
  return operation_f6213b8e3a5c();
}
