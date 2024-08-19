""""Resolver problema del taller de Camilo."""

import pulp as lp

x_1 = lp.LpVariable(name="metros_poli",
                    lowBound=0,
                    upBound=40,
                    cat=lp.LpContinuous)

x_2 = lp.LpVariable(name="metros_eco",
                    lowBound=0,
                    upBound=None,
                    cat=lp.LpContinuous)

prob = lp.LpProblem(name="Taller de Camilo",
                    sense=lp.LpMaximize)

prob += x_1 + x_2 <= 80, "No_ecceder_horas_hilado"
prob += 2 * x_1 + x_2 <= 100, "No_ecceder_horas_tintado"

prob += 3 * x_1 + 2 * x_2, "Maximizar_los_ingresos"
prob.solve()

print("Status: ", lp.LpStatus[prob.status])

print("Utilidad: ", lp.value(prob.objective))

for v in prob.variables():
    print(v, ": ", lp.value(v))